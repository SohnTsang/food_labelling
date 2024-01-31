document.addEventListener('DOMContentLoaded', function() {
    // Function to capture and download labels as PNG
    function captureAndDownloadPngLabels() {
        const labelElements = document.querySelectorAll('.label');
        labelElements.forEach((labelElement, index) => {
            html2canvas(labelElement).then(canvas => {
                let image = canvas.toDataURL("image/png");
                triggerFileDownload(image, `label_${index}.png`);
            });
        });
    }

    // Function to capture and download labels as PDF
    function captureAndDownloadPdfLabels() {
        const { jsPDF } = window.jspdf;
        const pdf = new jsPDF();

        const labelElements = document.querySelectorAll('.label');
        labelElements.forEach((labelElement, index) => {
            if (index > 0) {
                pdf.addPage(); // Add a new page for each label (except the first one)
            }

            html2canvas(labelElement).then(canvas => {
                const imgData = canvas.toDataURL('image/png');
                pdf.addImage(imgData, 'PNG', 0, 0);
                if (index < labelElements.length - 1) {
                    pdf.addPage(); // Add a new page for the next label
                } else {
                    // Check if the first page is blank and remove it
                    pdf.deletePage(1);
                    pdf.save("labels.pdf"); // Save the PDF when all labels are added
                }
            });
        });
    }

    function isBlankPage(pageData) {
    // You can define your criteria for a blank page here.
    // For example, if the pageData contains a small amount of data,
    // you can consider it blank.
        return pageData.length < 1000; // Adjust the threshold as needed
    }

    // Function to trigger file download
    function triggerFileDownload(dataUri, fileName) {
        let link = document.createElement('a');
        link.href = dataUri;
        link.download = fileName;

        // Trigger a click event on the link to initiate download
        link.click();
    }

    // Add click event listener to all download buttons
    const downloadButtons = document.querySelectorAll('.download-label');
    downloadButtons.forEach(button => {
        button.addEventListener('click', function() {
            const format = this.getAttribute('data-format');
            if (format === 'png') {
                captureAndDownloadPngLabels();
            } else if (format === 'pdf') {
                captureAndDownloadPdfLabels();
            }
        });
    });

    function synchronizeEdits(e) {
        if (e.target.classList.contains('editable-content')) {
            let group = e.target.getAttribute('data-group');
            let allSameGroupElements = document.querySelectorAll(`[data-group='${group}']`);
            allSameGroupElements.forEach(function(element) {
                if (element !== e.target) {
                    element.innerHTML = e.target.innerHTML;
                }
            });
        }
    }
    document.addEventListener('input', synchronizeEdits);

});