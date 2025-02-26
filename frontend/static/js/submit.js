document.addEventListener("DOMContentLoaded", function() {
    const submitBtn = document.getElementById("submit")
    const route = window.location.pathname.split("/auth")[1]
    if (route == "/register") {
        const form = document.getElementById("registerForm")
        submitBtn.addEventListener("click", function(e) {
            e.preventDefault();
            const formData = new FormData(form)
            Object.fromEntries(formData)
        })
    }
})