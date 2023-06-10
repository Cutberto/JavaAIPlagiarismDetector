document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll("select");
  var instances = M.FormSelect.init(elems);
});

document.getElementById("compareButton").addEventListener("click", function () {
  var selectedRoute = document.getElementById("backendSelect").value;
  var text1 = document.getElementById("text1").value;
  var text2 = document.getElementById("text2").value;

  // Hide Compare button
  hideCompareButton();

  // Show loading spinner
  showLoadingSpinner();

  var xhr = new XMLHttpRequest();
  xhr.open("POST", selectedRoute, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      // Hide loading spinner
      hideLoadingSpinner();

      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        var value = response.value;
        updateProgressBar(value);
        showResultSection(value);
      } else {
        // Handle error
        console.error("Request failed with status:", xhr.status);
      }

      // Show Compare button
      showCompareButton();
    }
  };

  var data = JSON.stringify({ text1: text1, text2: text2 });
  xhr.send(data);
});

function updateProgressBar(value) {
  var progressBar = document.getElementById("progressBar");
  progressBar.style.width = value * 100 + "%";
}

function showResultSection(value) {
  var resultSection = document.getElementById("resultSection");
  var resultLabel = document.getElementById("resultLabel");
  var trimmedValue = (value * 100).toFixed(2);
  resultLabel.innerText = "The similarity is " + trimmedValue + "%";
  resultSection.classList.remove("hide");
}

function showCompareButton() {
  var compareButton = document.getElementById("compareButton");
  compareButton.classList.remove("hide");
}

function hideCompareButton() {
  var compareButton = document.getElementById("compareButton");
  compareButton.classList.add("hide");
}

function showLoadingSpinner() {
  var compareButton = document.getElementById("compareButton");
  compareButton.innerHTML = `
    <div class="preloader-wrapper small active">
      <div class="spinner-layer spinner-blue-only">
        <div class="circle-clipper left">
          <div class="circle"></div>
        </div>
        <div class="gap-patch">
          <div class="circle"></div>
        </div>
        <div class="circle-clipper right">
          <div class="circle"></div>
        </div>
      </div>
    </div>
  `;
}

function hideLoadingSpinner() {
  var compareButton = document.getElementById("compareButton");
  compareButton.innerHTML = "Compare";
}
