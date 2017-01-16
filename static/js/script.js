var data = {};
$('.clockpicker').clockpicker();
//create grid buttons
function clickableGrid(rows, cols, callback) {
    var i = 0;
    var grid = document.getElementById("grid");
    grid.className = 'grid';
    for (var r = 0; r < rows; ++r) {
        var tr = grid.appendChild(document.createElement('tr'));
        for (var c = 0; c < cols; ++c) {
            var cell = tr.appendChild(document.createElement('td'));
            cell.innerHTML = ++i;
            cell.addEventListener('click', (function(el, r, c, i) {
                return function() {
                    callback(el, r, c, i);
                }
            })(cell, r, c, i), false);
        }
    }
    return grid;
}


var grid = clickableGrid(15, 20, function(el, row, col, i) {
    console.log("You clicked on element:", el);
    console.log("You clicked on row:", row);
    console.log("You clicked on col:", col);
    console.log("You clicked on item #:", i);

    if (el.className == "clicked") {
        el.className = "";
    } else {
        el.className = 'clicked';
        data["row"] = row;
        data["col"] = col;
        data["item"] = i;
    }


});

$("#submit").click(function() {
    var name = $("#athleteName").val();
    var time = $("#time").val();
    data["name"] = name;
    data["time"] = time;
    data["day"] = timestamp();
    submitInfo(data);
})


function submitInfo(data) {
    $.ajax({
        type: 'POST',
        url: '/submit',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'text',
        success: function(msg, status, jqXHR) {
            console.log("Success");
            alert("Submitted data");

        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert(textStatus, errorThrown);
        }
    });

}

function timestamp() {
    var d = new Date();
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var days = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'];
    var day = days[d.getDay()];
    var hr = d.getHours();
    var min = d.getMinutes();
    if (min < 10) {
        min = "0" + min;
    }
    var ampm = hr < 12 ? "am" : "pm";
    var date = d.getDate();
    var month = months[d.getMonth()];
    var year = d.getFullYear();
    var seconds = d.getSeconds();

    var timestamp = date + "-" + month + "-" + year; //day+ " " + hr + ":" + min + ":" + seconds + ampm + " " + date + " " + month + " " + year;

    return timestamp;
}
