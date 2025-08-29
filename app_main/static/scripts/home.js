document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.querySelectorAll('.message-container .message').forEach(function(msg) {
            msg.remove();
        });
    }, 4000); // 3000ms = 3 seconds
});