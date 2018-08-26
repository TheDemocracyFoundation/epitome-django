/**
 * Clockpicker definition.
 * Two instances (start input and end input) are used.
 */
var sinput = $('#sinput');
var einput = $('#einput');
sinput.clockpicker({
    autoclose: true
});
einput.clockpicker({
    autoclose: true
});

$('#shour').click(function(e){
    // Have to stop propagation here
    e.stopPropagation();
    sinput.clockpicker('show')
            .clockpicker('toggleView', 'hours');
});

$('#ehour').click(function(e){
    // Have to stop propagation here
    e.stopPropagation();
    einput.clockpicker('show')
            .clockpicker('toggleView', 'hours');
});

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
var taggle = new Taggle('categories');
function submitAll(){
    var stringBuilder = "";
    var inputs = document.getElementsByClassName("target");
    var categories = taggle.getTags().values.toString();
    
    for(i = 0; i < inputs.length; i++){
        var link = inputs.item(i);
        if (i === 0){
            stringBuilder = stringBuilder + inputs.item(i).value;
        }else{
            stringBuilder = stringBuilder + "," + inputs.item(i).value;
        }
    }
    

    //document.getElementById("form-voting-options").value = stringBuilder;
    document.getElementById("form-categories").value = categories;
    
    console.log(stringBuilder);
    console.log(categories);

    document.getElementById("form-body").submit();
}