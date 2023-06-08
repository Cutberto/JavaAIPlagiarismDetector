document.getElementById("compareButton").addEventListener("click", function () {
  var text1 = document.getElementById("text1").value;
  var text2 = document.getElementById("text2").value;

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "http://127.0.0.1:5000/compare", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      var value = response.value;
      updateProgressBar(value);
    }
  };
  var data = JSON.stringify({ text1: text1, text2: text2 });
  xhr.send(data);
});

function updateProgressBar(value) {
  var progressBar = document.getElementById("progressBar");
  progressBar.style.width = value * 100 + "%";
}
