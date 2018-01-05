import tempfile
import pygit2
import os.path
import shutil
import re

# http: //www.pygit2.org/recipes/git-clone-ssh.html
  #https: //docs.python.org/2/library/tempfile.html

RepoUser = 'git'
RepoPub = os.path.expanduser('~/.ssh/id_rsa.pub')
RepoPrv = os.path.expanduser('~/.ssh/id_rsa')
repoUrl = mkdtemp()
pygit2.init_repository(repoUrl)# blank local origin

# Setup master repo on load.
masterRepoDir = mkdtemp()# this dir gets a repo with a checked out copy of master
keypair = pygit2.Keypair(RepoUser, RepoPub, RepoPrv, "")
callbacks = pygit2.RemoteCallbacks(credentials = keypair)
masterRepo = pygit2.clone_repository(repoUrl, masterRepoDir, callbacks = callbacks)
remoteRegex = re.compile(r'^refs/remotes/origin/')
localRegex = re.compile(r'^refs/heads/')

class activeProposalsClass():
  master=[]

def activeProposals():
  return(activeProposalsClass.master)

def regenerateActiveProposals(): #Return a list of active proposals.
  out = []
  mergeRepo = pygit2.clone_repository( masterRepoDir,tempfile.mkdtemp())
  branches = filter(remoteRegex, list(mergeRepo.references))
  for branchto in branches:
    to_id = mergeRepo.lookup_reference(branchto).target
    merge_result, _ = mergeRepo.merge_analysis(to_id)
    if merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:# anything that ff merges is good.
      out.append(re.sub(remoteRegex,'',branchto))
    elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:# anything that merges without conflict is good
      mergeRepo.merge(to_id)
      if repo.index.conflicts is None:
        out.append(re.sub(remoteRegex,'',branchto))
      mergeRepo.state_cleanup()
      mergeRepo.reset(pygit2.GIT_RESET_HARD)
  activeProposalsClass.master = out
  shutil.rmtree(mergeRepo.workdir,ignore_errors=True)

regenerateActiveProposals()

def blankProposal(branch = None, repoDir = None): #User wants a repo to edit, return a repo 
  if branch is None:
    branch = 'master'
  if repoDir is None:
    repoDir = mkdtemp()
  return pygit2.clone_repository(masterRepoDir, repoDir, checkout_branch = branch)

def submitProposal(branch, repo, comment): #User wants to submit their changes# http: //www.pygit2.org/objects.html#creating-commits
  ref = 'refs/heads/' + branch
  user = repo.default_signature
  repo.index.add_all()
  tree = repo.TreeBuilder().write()
  repo.create_commit(ref, user, user, comment, tree, [])
  repo.index.write()
  pushRef = '%s:%s' % (ref,ref)
  push(repo, ref = pushRef) # push to masterRepo
  regenerateActiveProposals()
  push(masterRepo, ref = pushRef) # push to origin
  
def acceptProposal(branch): 
  test = False
  for prop in activeProposals():
    if prop == branch:
      test = True
  if test != True:
    raise AssertionError('Requested branch \'%s\' is not valid active proposal' % (branch))
  mergeRepo = pygit2.clone_repository( masterRepoDir,tempfile.mkdtemp())
  merge_id = mergeRepo.lookup_reference('refs/remotes/origin/%s' % (branch)).target
  merge_result, _ = mergeRepo.merge_analysis(merge_id)
  if merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
    mergeRepo.checkout_tree(mergeRepo.get(merge_id))
    master_ref = mergeRepo.lookup_reference('refs/heads/master')
    master_ref.set_target(merge_id)
    mergeRepo.head.set_target(merge_id)
  elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
    mergeRepo.merge(merge_id)
    user = mergeRepo.default_signature
    tree = mergeRepo.index.write_tree()
    commit = repo.create_commit('HEAD',user,user,'Merge!',tree, [mergeRepo.head.target, merge_id])
    repo.state_cleanup()
  push(mergeRepo)
  masterRepo.checkout_tree(masterRepo.get(masterRepo.lookup_reference('refs/heads/master')))
  regenerateActiveProposals()
  push(masterRepo)
  shutil.rmtree(mergeRepo.workdir,ignore_errors=True)
  newBranch = strftime('master-%Y-%m-%d-%H-%M-%S')
  masterRepo.branches.local.create(newBranch)
  push(masterRepo,'origin','/refs/heads/'+newBranch)

def push(repo, remote_name = 'origin', ref = 'refs/heads/master:refs/heads/master'): #https://github.com/MichaelBoselowitz/pygit2-examples/blob/master/examples.py
  for remote in repo.remotes:
    if remote.name == remote_name:
      remote.push(ref)


def pull(repo, remote_name = 'origin', branch = 'master'): #https://github.com/MichaelBoselowitz/pygit2-examples/blob/master/examples.py
  for remote in repo.remotes:
    if remote.name == remote_name:
      remote.fetch()
      remote_master_id = repo.lookup_reference('refs/remotes/origin/%s' % (branch)).target
      merge_result, _ = repo.merge_analysis(remote_master_id)# Up to date, do nothing
      if merge_result & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
        return# We can just fastforward
      elif merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
        repo.checkout_tree(repo.get(remote_master_id))
        try:
          master_ref = repo.lookup_reference('refs/heads/%s' % (branch))
          master_ref.set_target(remote_master_id)
        except KeyError:
          repo.create_branch(branch, repo.get(remote_master_id))
        repo.head.set_target(remote_master_id)
      elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
        repo.merge(remote_master_id)
        if repo.index.conflicts is not None:
          for conflict in repo.index.conflicts:
            print 'Conflicts found in:', conflict[0].path
          raise AssertionError('Conflicts, ahhhhh!!')
        user = repo.default_signature
        tree = repo.index.write_tree()
        commit = repo.create_commit('HEAD',user,user,'Merge!',tree, [repo.head.target, remote_master_id])# We need to do this or git CLI will think we are still merging.
        repo.state_cleanup()
      else :
        raise AssertionError('Unknown merge analysis result')
