import styles from "./Navbar.module.scss";

const Navbar = ({
  toggleTheme,
  darkMode,
}: {
  toggleTheme: () => void;
  darkMode: boolean;
}) => {
  return (
    <div className={styles.navbar}>
      <a href="#header">Home</a>
      <a href="#about">About</a>
      <a href="#services">Services</a>
      <a href="#team">Team</a>
      <a href="#blog">Blog</a>
      <a href="#contact">Contact</a>
      <button onClick={toggleTheme} className={styles.button}>
        {darkMode ? "Light Mode" : "Dark Mode"}
      </button>
    </div>
  );
};

export default Navbar;
