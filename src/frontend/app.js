const apiBase = `${window.location.protocol}//${window.location.host}`;

// Start the race
function startRace() {
  fetch(`${apiBase}/start_race`, { method: 'POST' })
    .then(res => res.json())
    .then(data => {
      alert(`🏁 Race started at ${new Date(data.start_time * 1000).toLocaleTimeString()}`);
    })
    .catch(console.error);
}

// Submit a participant's finish
function submitFinish() {
  const nameInput = document.getElementById('participantName');
  const name = nameInput.value.trim();
  console.log("Name: ", name)
  if (!name) {
    alert("Please enter a participant name.");
    return;
  }

  fetch(`${apiBase}/submit_finish`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ participant: name })
  })
    .then(res => res.json())
    .then(data => {
      alert(`✅ Finish recorded for ${data.participant}`);
      nameInput.value = '';
    })
    .catch(console.error);
}

// Fetch and display results
function fetchResults() {
  fetch(`${apiBase}/results`)
    .then(res => res.json())
    .then(results => {
      const list = document.getElementById('results');
      list.innerHTML = '';
      results.forEach(r => {
        const li = document.createElement('li');
        li.textContent = `${r.participant}: ${r.elapsed_time}s`;
        list.appendChild(li);
      });
    })
    .catch(console.error);
}