document.addEventListener('DOMContentLoaded', function() {
    // Modal elements
    const loginModal = document.getElementById("loginModal");
    const registerModal = document.getElementById("registerModal");
    const courseDetailsModal = document.getElementById("courseDetailsModal");

    // Buttons
    const loginBtn = document.getElementById("loginBtn");
    const registerBtn = document.getElementById("registerBtn");

    // Close spans (×)
    const closeLogin = loginModal.querySelector(".close");
    const closeRegister = registerModal.querySelector(".close");
    const closeCourseDetails = courseDetailsModal.querySelector(".close");

    // Switch links
    const goToRegister = document.getElementById("goToRegister");
    const goToLogin = document.getElementById("goToLogin");

    // Course details buttons
    const viewCourseButtons = document.querySelectorAll(".view-course-details");

    // Forms
    const contactForm = document.getElementById("contactForm");
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");

    // --- Modal Functions ---
    const openModal = (modal) => {
        modal.style.display = "block";
    };

    const closeModal = (modal) => {
        modal.style.display = "none";
    };

    // --- Event Listeners ---
    loginBtn.addEventListener("click", () => openModal(loginModal));
    registerBtn.addEventListener("click", () => openModal(registerModal));

    closeLogin.addEventListener("click", () => closeModal(loginModal));
    closeRegister.addEventListener("click", () => closeModal(registerModal));
    closeCourseDetails.addEventListener("click", () => closeModal(courseDetailsModal));

    goToRegister.addEventListener("click", (e) => {
        e.preventDefault();
        closeModal(loginModal);
        openModal(registerModal);
    });

    goToLogin.addEventListener("click", (e) => {
        e.preventDefault();
        closeModal(registerModal);
        openModal(loginModal);
    });

    // --- Fetch Course Data from Backend ---
    const fetchCourses = async () => {
        try {
            const response = await fetch('http://localhost:3001/api/courses'); // Backend URL
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data; // Return the fetched data
        } catch (error) {
            console.error('Failed to fetch courses:', error);
            return []; // Return an empty array in case of error
        }
    };

    // --- Display Course Details ---
    const displayCourseDetails = (course) => {
        document.getElementById("courseDetailsTitle").textContent = course.title;

        let content = `<p>${course.description}</p>`;

        if (course.materials && course.materials.length > 0) {
            content += "<h3>Tài liệu:</h3><ul>";
            course.materials.forEach(material => {
                content += `<li><a href="#">${material}</a></li>`; // Adjust the link as needed
            });
            content += "</ul>";
        }

        if (course.exercises) {
            content += `<h3>Bài tập:</h3><a href="#">${course.exercises}</a>`; // Adjust the link as needed
        }

        if (course.video) {
            content += `<h3>Video bài giảng:</h3><iframe src="${course.video}" frameborder="0" allowfullscreen></iframe>`;
        }

        document.getElementById("courseDetailsContent").innerHTML = content;
        openModal(courseDetailsModal); // Open the modal
    };

    // --- Handle View Course Details Click ---
    viewCourseButtons.forEach(button => {
        button.addEventListener("click", async () => { // Make the event listener async
            const courseId = button.closest('.course-item').dataset.courseId;
            try {
                const courses = await fetchCourses(); // Fetch courses from backend
                const course = courses.find(course => course.id === courseId);
                if (course) {
                    displayCourseDetails(course);
                } else {
                    alert("Course not found.");
                }
            } catch (error) {
                console.error("Error fetching or displaying course:", error);
                alert("Failed to load course details.");
            }
        });
    });

    // --- Initialize the Page ---
    const init = async () => {
        try {
            await fetchCourses(); // Fetch courses on page load
        } catch (error) {
            console.error("Error initializing:", error);
            alert("Failed to load initial data.");
        }
    };

    init();
});