import React from "react";
import styles from "./Footer.module.scss";

interface FooterProps {
  companyName: string;
}

const Footer: React.FC<FooterProps> = ({ companyName }) => {
  return (
    <footer className={styles.footer}>
      <div className="footer-content">
        <p>
          &copy; {new Date().getFullYear()} {companyName}
        </p>
      </div>
    </footer>
  );
};

export default Footer;
