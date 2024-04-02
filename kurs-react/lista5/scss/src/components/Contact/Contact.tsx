import React from "react";
import styles from "./Contact.module.scss";

interface ContactProps {
  handleSubmit: (event: React.FormEvent<HTMLFormElement>) => void;
}

const Contact: React.FC<ContactProps> = ({ handleSubmit }) => {
  return (
    <>
      <h2>Contact Us</h2>
      <form onSubmit={handleSubmit} className={styles.contactForm}>
        <div>
          <input type="text" placeholder="Name" required />
        </div>
        <div>
          <input type="email" placeholder="Email" required />
        </div>
        <div>
          <textarea rows={5} placeholder="Message" required></textarea>
        </div>
        <button type="submit">Send Message</button>
      </form>
    </>
  );
};

export default Contact;
