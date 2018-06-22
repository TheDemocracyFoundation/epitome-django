/**
 * Option form field generator.
 * Used to create dynamic forms to use as voting options.
 */
var optionGroup = document.getElementById("choice");
var i = 0;

// Adds new input form.
function addOption(){
    var fieldWrapper = document.createElement("div");
            fieldWrapper.id = "choice" + i;
            fieldWrapper.className = "input-group mb-3";
        fieldWrapper.innerHTML =   `<input type="text" class="form-control target" placeholder="New Option" aria-label="Recipient's username" aria-describedby="basic-addon2">
                                    <div class="input-group-append">
                                        <button class="btn btn-outline-danger" type="button" onclick="removeOption(`+ i +`)"><b>x</b></button>
                                    </div>`;
    i++;
    optionGroup.appendChild(fieldWrapper);
}

// Add 3 forms on pageload.
addOption();
addOption();

// Removes a form based on id as long as 3 forms exist.
function removeOption(rem){
    var remove = document.getElementById("choice"+rem);
    var count = document.getElementById("choice").childElementCount;
    
    if (count > 3){
        document.getElementById("choice").removeChild(remove);
    }else{
        $("#exampleModalCenter").modal();
    }
}

// Submit Contents
function submitAll(){
    var stringBuilder = "";
    var inputs = document.getElementsByClassName("target");
    
    for(i = 0; i < inputs.length; i++){
        var link = inputs.item(i);
        if (i === 0){
            stringBuilder = stringBuilder + inputs.item(i).value;
        }else{
            stringBuilder = stringBuilder + "," + inputs.item(i).value;
        }
    }
    
    console.log(stringBuilder);
    document.getElementById("payload").value = stringBuilder;
    
    console.log(document.getElementById("form-body"))
    document.getElementById("form-body").submit();
}