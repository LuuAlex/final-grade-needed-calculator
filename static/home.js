console.log("run")

function get_inputs() {
    return {
        grade: document.getElementById('grade').value
    }
}

fetch('/get_data')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        console.log('GET response:');
        console.log(text.greeting);
});

