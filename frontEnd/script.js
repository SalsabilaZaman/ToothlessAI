async function sendMessage() {
  const message = document.getElementById('userMessage').value;

  const response = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  if (response.ok) {
    const data = await response.json();
    document.getElementById('mood').textContent = data.mood;
    document.getElementById('reply').textContent = data.reply;
  } else {
    alert('Something went wrong.');
  }
}
