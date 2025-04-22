<script>
    function toggleTheme() {
        document.body.classList.toggle('dark-mode');
    }

    function sendMessage() {
        const input = document.getElementById("user-input");
        const message = input.value.trim();
        if (!message) return;

        const messagesDiv = document.getElementById("messages");
        messagesDiv.innerHTML += `<div class='message user'>${message}</div>`;
        input.value = "";

        const typing = document.getElementById("typing");
        typing.style.display = 'block';

        fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        })
        .then(res => res.json())
        .then(data => {
            setTimeout(() => {
                messagesDiv.innerHTML += `<div class='message bot'>${data.reply}</div>`;
                typing.style.display = 'none';
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            }, 700);
        });
    }
</script>
