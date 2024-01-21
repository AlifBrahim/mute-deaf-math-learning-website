function startReadingProgress() {
           const progressBar = document.getElementById('reading-progress');
           let progress = 0;
           const readingTime = 60000; // 60 seconds for example
           const updateInterval = 1000; // Update every second

           const interval = setInterval(() => {
               progress += updateInterval;
               const progressPercentage = Math.min((progress / readingTime) * 100, 100);
               progressBar.style.width = progressPercentage + '%';
               progressBar.textContent = Math.round(progressPercentage) + '%';

               if (progressPercentage >= 100) {
                   clearInterval(interval);
                   // Send POST request to the server to update mastery points
                   fetch('{{ url_for("darab2digit") }}', { method: 'POST' })
                       .then(response => response.json())
                       .then(data => {
                           if (data.success) {
                               alert('Congratulations! You\'ve earned 5 mastery points.');
                               window.location.href = data.next_url;
                           }
                       });
               }
           }, updateInterval);
       }

       // Start the reading progress when the document is ready
       document.addEventListener('DOMContentLoaded', startReadingProgress);