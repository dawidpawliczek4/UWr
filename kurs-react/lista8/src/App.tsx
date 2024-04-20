import React, { useState } from "react";
import "./styles.css";

const companyData = {
  name: "Acme Corporation",
  slogan: "Innovation at its best",
  about:
    "We are a leading provider of innovative solutions in various industries. Our team is dedicated to delivering high-quality products and services to our clients worldwide.",
  services: [
    {
      id: 1,
      name: "Web Development",
      description: "Creating modern and responsive websites.",
    },
    {
      id: 2,
      name: "Mobile App Development",
      description: "Building mobile applications for iOS and Android.",
    },
    {
      id: 3,
      name: "UI/UX Design",
      description:
        "Designing intuitive user interfaces for optimal user experience.",
    },
    {
      id: 4,
      name: "Digital Marketing",
      description:
        "Promoting products and services through various online channels.",
    },
  ],
  teamMembers: [
    {
      id: 1,
      name: "Alice Young",
      position: "CEO",
      bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero et nisi cursus, sit amet laoreet odio rutrum.",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 2,
      name: "Jane Smith",
      position: "CTO",
      bio: "Duis aliquam purus ac ante volutpat, nec lobortis tortor sagittis. Sed finibus eleifend efficitur.",
      image: "https://via.placeholder.com/150",
    },
    {
      id: 3,
      name: "Alice Johnson",
      position: "Lead Designer",
      bio: "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris consectetur, velit et efficitur fringilla, ligula felis dignissim.",
      image: "https://via.placeholder.com/150",
    },
  ],
  blogPosts: [
    {
      id: 1,
      title: "The Future of Technology",
      date: "March 10, 2024",
      content:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero et nisi cursus, sit amet laoreet odio rutrum.",
    },
    {
      id: 2,
      title: "Design Trends for 2024",
      date: "February 28, 2024",
      content:
        "Duis aliquam purus ac ante volutpat, nec lobortis tortor sagittis. Sed finibus eleifend efficitur.",
    },
    {
      id: 3,
      title: "The Power of Social Media",
      date: "February 15, 2024",
      content:
        "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris consectetur, velit et efficitur fringilla, ligula felis dignissim.",
    },
    {
      id: 4,
      title: "Artificial Intelligence in Business",
      date: "January 30, 2024",
      content:
        "Suspendisse eget sapien vitae eros tincidunt ultrices. Morbi nec sem nisi. Nulla ultrices odio et eros varius, a eleifend velit tristique.",
    },
    {
      id: 5,
      title: "The Impact of Virtual Reality",
      date: "January 15, 2024",
      content:
        "Integer auctor neque mauris, eget sagittis justo tristique sit amet. Nam at nibh et nulla suscipit blandit eu nec mi.",
    },
  ],
};

const App = () => {
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
  };
  const [darkMode, setDarkMode] = useState(false);

  const toggleTheme = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div
      className={`portfolio ${
        darkMode ? "dark" : ""
      } text-[#333] dark:text-[#fff] dark:bg-[#111]`}
    >
      <div className="sticky top-0 py-4 text-center z-10 bg-[#f0f0f0] dark:bg-[#222]">
        <a href="#header" className="px-5 ">
          Home
        </a>
        <a href="#about" className="px-5">
          About
        </a>
        <a href="#services" className="px-5">
          Services
        </a>
        <a href="#team" className="px-5">
          Team
        </a>
        <a href="#blog" className="px-5">
          Blog
        </a>
        <a href="#contact" className="px-5">
          Contact
        </a>
        <button
          onClick={toggleTheme}
          className="cursor-pointer px-4 py-2 bg-[#333] text-[#fff] rounded-md hover:bg-[#555]
          dark:bg-[#ddd] dark:text-[#333] dark:hover:bg-[#ccc]
          "
        >
          {darkMode ? "Light Mode" : "Dark Mode"}
        </button>
      </div>
      <header id="header" className="py-12 text-center">
        <div className="">
          <h1 className="text-5xl mb-3 font-bold">{companyData.name}</h1>
          <p className="text-2xl">{companyData.slogan}</p>
        </div>
      </header>
      <div className="rounded-lg my-3 bg-[#eee] dark:bg-[#333]">
        <section id="about" className="section about">
          <div className="section-content">
            <h2 className="font-semibold">About Us</h2>
            <p>{companyData.about}</p>
          </div>
        </section>
        <section id="services" className="section services">
          <div className="section-content">
            <h2>Our Services</h2>
            <ul>
              {companyData.services.map((service) => (
                <li key={service.id}>
                  <h3>{service.name}</h3>
                  <p>{service.description}</p>
                </li>
              ))}
            </ul>
          </div>
        </section>
        <section id="team" className="section team">
          <div className="section-content">
            <h2>Meet Our Team</h2>
            <div className="team-members">
              {companyData.teamMembers.map((member) => (
                <div key={member.id} className="team-member">
                  <img src={member.image} alt={member.name} />
                  <div>
                    <h3>{member.name}</h3>
                    <p>{member.position}</p>
                    <p>{member.bio}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
        <section id="blog" className="section blog">
          <div className="section-content">
            <h2>Latest Blog Posts</h2>
            <div className="blog-posts">
              {companyData.blogPosts.map((post) => (
                <div key={post.id} className="blog-post">
                  <h3>{post.title}</h3>
                  <p>{post.date}</p>
                  <p>{post.content}</p>
                  <button>Read More</button>
                </div>
              ))}
            </div>
          </div>
        </section>
        <section id="contact" className="section contact">
          <div className="section-content">
            <h2>Contact Us</h2>
            <form onSubmit={handleSubmit} className="contact-form">
              <div className="form-group">
                <input type="text" placeholder="Name" required />
              </div>
              <div className="form-group">
                <input type="email" placeholder="Email" required />
              </div>
              <div className="form-group">
                <textarea rows={5} placeholder="Message" required></textarea>
              </div>
              <button type="submit">Send Message</button>
            </form>
          </div>
        </section>
      </div>
      <footer className="footer">
        <div className="footer-content">
          <p>
            &copy; {new Date().getFullYear()} {companyData.name}
          </p>
        </div>
      </footer>
    </div>
  );
};

export default App;
