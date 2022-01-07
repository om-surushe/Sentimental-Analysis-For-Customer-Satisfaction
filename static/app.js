

        function startConverting(element) {
            // element.preventDefault();
            var result = document.getElementById(element);

            if ('webkitSpeechRecognition' in window) {
                var speechRecognizer = new webkitSpeechRecognition();
                speechRecognizer.continuous = true;
                speechRecognizer.interimResults = true;
                speechRecognizer.lang = 'en-US';
                speechRecognizer.start();

                var finalTranscripts = '';

                speechRecognizer.onresult = function (event) {
                    var interimTranscripts = '';
                    for (var i = event.resultIndex; i < event.results.length; i++) {
                        var transcript = event.results[i][0].transcript;
                        transcript.replace("\n", "<br>");
                        if (event.results[i].isFinal) {
                            finalTranscripts += transcript;
                        } else {
                            interimTranscripts += transcript;
                        }
                    }
                    result.value = finalTranscripts + interimTranscripts;
                };
                speechRecognizer.onerror = function (event) {

                };
            } else {
                result.value = 'Your browser is not supported. Please download Google chrome or Update your Google chrome!!';
            }
        }
