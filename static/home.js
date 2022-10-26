console.log("run")

function get_inputs() {
    return {
        grade: document.getElementById('grade').value
    }
}

$.post( "/postmethod", {
    javascript_data: get_inputs()
});

