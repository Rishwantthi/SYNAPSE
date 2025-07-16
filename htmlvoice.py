<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agri-Mithra: Voice-Enabled AI Support Demo</title>
    <style>
        body { font-family: 'Arial', sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; line-height: 1.6; }
        .container { max-width: 850px; margin: auto; background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
        h1, h2 { color: #28a745; text-align: center; margin-bottom: 25px; }
        p { text-align: center; margin-bottom: 20px; color: #555; }
        form { margin-top: 25px; padding: 25px; border: 1px solid #e0e0e0; border-radius: 8px; background-color: #fcfcfc; }
        label { display: block; margin-bottom: 8px; font-weight: bold; color: #444; }
        input[type="text"], select, input[type="file"] {
            width: calc(100% - 22px); /* Account for padding */
            padding: 11px;
            margin-bottom: 18px;
            border: 1px solid #bbb;
            border-radius: 5px;
            font-size: 16px;
            box-sizing: border-box; /* Include padding in width */
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s ease;
        }
        button:hover { background-color: #0056b3; }
        .message { margin-top: 15px; padding: 12px; border-radius: 5px; text-align: center; }
        .success { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .error { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        .request-list { margin-top: 40px; }
        .request-item {
            background-color: #e9f7ef;
            border-left: 6px solid #28a745;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 8px;
            position: relative;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .request-item p { margin: 8px 0; text-align: left; }
        .status-pending { color: #ff8c00; font-weight: bold; } /* Orange */
        .status-completed { color: #28a745; font-weight: bold; } /* Green */
        .status-image-requested, .status-image-received { color: #8a2be2; font-weight: bold; } /* Purple */
        .upload-section {
            margin-top: 15px;
            padding: 15px;
            background-color: #f0f8ff;
            border: 1px dashed #a8d6ff;
            border-radius: 6px;
            text-align: center;
        }
        .upload-section.hidden { display: none; }
        .upload-section button { background-color: #20c997; margin-top: 10px; }
        .upload-section button:hover { background-color: #1a9c7b; }
        .request-id-display {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #333;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.85em;
            font-weight: bold;
        }
        .spinner {
            border: 4px solid rgba(0, 0, 0, 0.1);
            border-left-color: #28a745;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            animation: spin 1s linear infinite;
            display: inline-block;
            vertical-align: middle;
            margin-left: 10px;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📞 Agri-Mithra: Call-Based AI Support Demo</h1>
        <p>For farmers who cannot type! Upload an audio file of your problem, and our AI will assist you.</p>

        <form id="audioQueryForm">
            <label for="contact">Your Contact Number (for SMS/WhatsApp communication):</label>
            <input type="text" id="contact" name="contact" placeholder="e.g., +919876543210" required>

            <label for="language">Choose Your Preferred Language (for response):</label>
            <select id="language" name="language" required>
                <option value="en">English</option>
                <option value="hi">हिन्दी (Hindi)</option>
                <option value="ta">தமிழ் (Tamil)</option>
                <option value="te">తెలుగు (Telugu)</option>
                <option value="kn">ಕನ್ನಡ (Kannada)</option>
                <option value="ml">മലയാളം (Malayalam)</option>
                <option value="bn">বাংলা (Bengali)</option>
                <option value="gu">ગુજરાતી (Gujarati)</option>
                <option value="mr">मराठी (Marathi)</option>
                <option value="pa">ਪੰਜਾਬੀ (Punjabi)</option>
            </select>

            <label for="audio_file">Upload Audio of Your Farming Problem (Simulates Voice Call Input):</label>
            <input type="file" id="audio_file" name="audio_file" accept="audio/*" required>

            <button type="submit">Submit Voice Problem (Simulate Call System)</button>
            <div id="formMessage" class="message" style="display: none;"></div>
        </form>

        <div class="request-list">
            <h2>📞 Your Support Requests</h2>
            <div id="requestsContainer">
                <p>No requests submitted yet.</p>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('audioQueryForm').addEventListener('submit', async function(event) {
            event.preventDefault();

            const formMessage = document.getElementById('formMessage');
            formMessage.style.display = 'none';

            const audioFile = document.getElementById('audio_file').files[0];
            const contact = document.getElementById('contact').value;
            const language = document.getElementById('language').value;

            if (!audioFile || !contact.trim() || !language.trim()) {
                formMessage.className = 'message error';
                formMessage.innerText = 'Please upload an audio file, provide contact, and select a language.';
                formMessage.style.display = 'block';
                return;
            }

            const formData = new FormData();
            formData.append('audio', audioFile); // 'audio' must match the key expected by Flask (request.files['audio'])
            formData.append('contact', contact);
            formData.append('language', language);

            try {
                const response = await fetch('/submit_audio_query', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();

                if (response.ok) {
                    formMessage.className = 'message success';
                    formMessage.innerText = data.message + " (Check your VS Code terminal for simulated SMS/WhatsApp messages)";
                    // Do NOT clear audio file input or contact/language to allow quick re-testing
                    fetchRequests(); // Refresh the list of requests
                } else {
                    formMessage.className = 'message error';
                    formMessage.innerText = data.message || 'An error occurred during submission.';
                }
            } catch (error) {
                formMessage.className = 'message error';
                formMessage.innerText = 'Network error or server unavailable. Please try again.';
                console.error('Error submitting audio query:', error);
            }
            formMessage.style.display = 'block';
        });

        async function fetchRequests() {
            try {
                const response = await fetch('/get_requests');
                const requests = await response.json();
                const requestsContainer = document.getElementById('requestsContainer');
                requestsContainer.innerHTML = ''; // Clear previous list

                if (requests.length === 0) {
                    requestsContainer.innerHTML = '<p>No requests submitted yet. Upload an audio problem above!</p>';
                    return;
                }

                requests.sort((a, b) => b.id - a.id); // Newest first

                requests.forEach(req => {
                    const item = document.createElement('div');
                    item.className = 'request-item';
                    let statusText = req.status;
                    let statusClass = '';

                    if (req.status === 'Pending') {
                        statusClass = 'status-pending';
                        statusText += ' <span class="spinner"></span>';
                    } else if (req.status === 'Pending - Image Requested') {
                        statusClass = 'status-image-requested';
                        statusText += ' <span class="spinner"></span>';
                    } else if (req.status === 'Image Received - Analyzing') {
                        statusClass = 'status-image-received';
                        statusText += ' <span class="spinner"></span>';
                    } else if (req.status.startsWith('Completed')) {
                        statusClass = 'status-completed';
                    }

                    item.innerHTML = `
                        <div class="request-id-display">ID: ${req.id}</div>
                        <p><strong>Transcribed Problem:</strong> ${req.problem}</p>
                        <p><strong>Contact:</strong> ${req.contact}</p>
                        <p><strong>Language:</strong> ${req.language.toUpperCase()}</p>
                        <p><strong>Status:</strong> <span class="${statusClass}">${statusText}</span></p>
                        <p><strong>Submitted:</strong> ${req.submitted_at}</p>
                        ${req.solution_sent ? `<p><strong>Simulated Response:</strong> ${req.solution_sent}</p>` : ''}
                        ${req.completed_at ? `<p><strong>Completed At:</strong> ${req.completed_at}</p>` : ''}
                        ${req.requires_image && !req.image_uploaded ? `
                            <div class="upload-section" id="uploadSection_${req.id}">
                                <p><strong>Image requested!</strong> To get precise guidance, please upload a clear photo of your crop/problem:</p>
                                <input type="file" id="imageUpload_${req.id}" accept="image/*" required>
                                <button onclick="uploadImage(${req.id})">Upload Image for Analysis</button>
                                <div id="uploadMessage_${req.id}" class="message" style="display:none;"></div>
                            </div>
                        ` : ''}
                    `;
                    requestsContainer.appendChild(item);
                });
            } catch (error) {
                console.error('Error fetching requests:', error);
                document.getElementById('requestsContainer').innerHTML = '<p class="error">Could not load requests.</p>';
            }
        }

        async function uploadImage(requestId) {
            const imageInput = document.getElementById(`imageUpload_${requestId}`);
            const uploadMessage = document.getElementById(`uploadMessage_${requestId}`);
            uploadMessage.style.display = 'none';

            if (imageInput.files.length === 0) {
                uploadMessage.className = 'message error';
                uploadMessage.innerText = 'Please select an image file to upload.';
                uploadMessage.style.display = 'block';
                return;
            }

            const imageFile = imageInput.files[0];
            const formData = new FormData();
            formData.append('image', imageFile);

            try {
                const response = await fetch(`/upload_image_for_request/${requestId}`, {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();

                if (response.ok) {
                    uploadMessage.className = 'message success';
                    uploadMessage.innerText = data.message;
                    document.getElementById(`uploadSection_${requestId}`).classList.add('hidden');
                    fetchRequests();
                } else {
                    uploadMessage.className = 'message error';
                    uploadMessage.innerText = data.message || 'Error uploading image.';
                }
            } catch (error) {
                uploadMessage.className = 'message error';
                uploadMessage.innerText = 'Network error during upload. Please check your connection.';
                console.error('Upload error:', error);
            }
            uploadMessage.style.display = 'block';
        }

        document.addEventListener('DOMContentLoaded', fetchRequests);
        setInterval(fetchRequests, 5000);
    </script>
</body>
</html>
