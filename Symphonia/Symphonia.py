import tempfile
import pygit2
import os.path
import shutil

# http: //www.pygit2.org/recipes/git-clone-ssh.html
  #https: //docs.python.org/2/library/tempfile.html

RepoUser = 'git'
RepoPub = os.path.expanduser('~/.ssh/id_rsa.pub')
RepoPrv = os.path.expanduser('~/.ssh/id_rsa')
repoUrl = mkdtemp()
pygit2.init_repository(repoUrl)# blank local origin

# Setup master repo on load.
masterRepoDir = mkdtemp()
keypair = pygit2.Keypair(RepoUser, RepoPub, RepoPrv, "")
callbacks = pygit2.RemoteCallbacks(credentials = keypair)
masterRepo = pygit2.clone_repository(repoUrl, masterRepoDir, callbacks = callbacks)
mergeRepo = pygit2.clone_repository( masterRepoDir,tempfile.mkdtemp())


def blankProposal(branch = None, repoDir = None): #User wants a repo to edit, return directory of local repo 
  if branch is None:
    branch = 'master'
  if repoDir is None:
    repoDir = mkdtemp()
  pygit2.clone_repository(masterRepoDir, repoDir, checkout_branch = branch)
  return repoDir;

def submitProposal(user, email, repoDir, comment): #User wants to submit their changes# http: //www.pygit2.org/objects.html#creating-commits
  ref = 'refs/heads/' + user
  author = pygit2.Signature(user, email)
  repo = pygit2.Repository(repoDir)
  repo.index.add_all()
  tree = repo.TreeBuilder().write()
  repo.create_commit(ref, author, author, comment, tree, [])
  repo.index.write()
  pushRef = '%s:%s' % (ref,ref)
  push(repo, ref = pushRef) # push to masterRepo
  push(masterRepo, ref = pushRef) # push to origin
  
def activeProposals(users, branch = 'master'): #Return a list of active proposals.
  out = []
  mergeRepo.remotes[0].fetch()
  branch_id = mergeRepo.lookup_reference('refs/remotes/origin/%s' % (branch))./target
  for user in users:
    mergeRepo.checkout_tree(mergeRepo.get(branch_id))
    remote_id = mergeRepo.lookup_reference('refs/remotes/origin/%s' % (user)).target
    merge_result, _ = mergeRepo.merge_analysis(remote_id)
    if merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:# anything that ff merges is good.
      out.append(user)
    elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:# anything that merges without conflict is good
      mergeRepo.merge(remote_id)
      if repo.index.conflicts is None:
        out.append(user)
      mergeRepo.state_cleanup()
      mergeRepo.reset(GIT_RESET_HARD)
  return (out)

def acceptProposal(branch): #Because active proposals must be fast - forwardable, we know we can just fast - forward an accepted active proposal
  test = activeProposals([branch])
  if test[0] != branch:
    raise AssertionError('Requested branch \'%s\' is not valid active proposal' % (branch))
  mergeRepo.remotes[0].fetch()
  merge_id = mergeRepo.lookup_reference('refs/remotes/origin/%s' % (branch)).target
  merge_result, _ = mergeRepo.merge_analysis(merge_id)
  if merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:# anything that ff merges is good.
    mergeRepo.checkout_tree(mergeRepo.get(merge_id))
    master_ref = mergeRepo.lookup_reference('refs/heads/master')
    master_ref.set_target(merge_id)
    mergeRepo.head.set_target(merge_id)
  elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:# anything that merges without conflict is good
    mergeRepo.merge(merge_id)
    user = repo.default_signature
    tree = repo.index.write_tree()
    commit = repo.create_commit('HEAD',user,user,'Merge!',tree, [repo.head.target, merge_id])# We need to do this or git CLI will think we are still merging.
    repo.state_cleanup()
  push(mergeRepo)
  push(masterRepo)

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
