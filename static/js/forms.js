// Select all the members
const memberContainer = document.querySelectorAll(".memberContainer");

// count the number from the dropdown
var e = document.getElementById("NoOfMembers");
function numberSelected() {
    var strUser = e.options[e.selectedIndex].value;
    containerSelected(strUser);
}

input_ids = [
    "3rdMemberName",
    "3rdMemberNumber",
    "3rdMemberEmail",
    "TransactionID3",
    "4thMemberName",
    "4thMemberNumber",
    "4thMemberEmail",
    "TransactionID4",
];


// turn display form none=>block
function containerSelected(num) {
    console.log(num);
    for (var i = 0; i < num; i++) {
        memberContainer[i].style.display = "block";
    }
    for (var i = num; i < 3; i++) {
        memberContainer[i].style.display = "none";
    }
    
    // Sets the required element to True for number of team members
    for (let input_index = 0; input_index < (num - 2) * 4; input_index++) {
        document.getElementById(input_ids[input_index]).required = true;
    }
    }
e.onchange = numberSelected;
numberSelected();
