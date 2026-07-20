document.addEventListener('DOMContentLoaded', () => {
    const fetchDataBtn = document.getElementById('fetchDataBtn');
    const dataDisplay = document.getElementById('dataDisplay');
    const geminiInput = document.getElementById('geminiInput');
    const sendToGeminiBtn = document.getElementById('sendToGeminiBtn');
    const geminiResponseDiv = document.getElementById('geminiResponse');

    // --- Example 1: Fetching simple data from backend ---
    fetchDataBtn.addEventListener('click', async () => {
        dataDisplay.textContent = 'Loading data...';
        try {
            // This assumes your Python backend has an endpoint like /api/data
            const response = await fetch('/api/data');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            dataDisplay.textContent = `Data from backend: ${JSON.stringify(data)}`;
        } catch (error) {
            console.error('Error fetching data:', error);
            dataDisplay.textContent = 'Failed to load data.';
        }
    });

    // --- Example 2: Interacting with your gemini_service.py ---
    sendToGeminiBtn.addEventListener('click', async () => {
        const prompt = geminiInput.value.trim();
        if (!prompt) {
            geminiResponseDiv.textContent = 'Please enter a prompt.';
            return;
        }

        geminiResponseDiv.textContent = 'Sending to Gemini service...';
        try {
            // This assumes your Python backend has an endpoint like /api/gemini
            const response = await fetch('/api/gemini', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: prompt })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(`HTTP error! status: ${response.status}, message: ${errorData.error || 'Unknown error'}`);
            }

            const data = await response.json();
            geminiResponseDiv.textContent = `Gemini Response: ${data.response}`;
        } catch (error) {
            console.error('Error sending to Gemini:', error);
            geminiResponseDiv.textContent = `Failed to get Gemini response: ${error.message}`;
        }
    });
});