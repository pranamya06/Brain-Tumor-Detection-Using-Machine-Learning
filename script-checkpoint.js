%%javascript

// Load the contents of the script.js file
var scriptContent = `
// Contents of script.js file

function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function() {
        var preview = document.getElementById('preview');
        preview.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
}

async function classifyImage() {
    var fileInput = document.getElementById('imageUpload');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('file', file);

    var response = await fetch('/classify', {
        method: 'POST',
        body: formData
    });

    var result = await response.json();
    var resultDiv = document.getElementById('result');
    resultDiv.innerText = 'Prediction: ' + result.prediction + ', Confidence: ' + result.confidence;
}
`;

// Execute the JavaScript code
eval(scriptContent);
