import styles from './Header.module.scss';

const Header = ({
  companyName,
  companySlogan,
}: {
  companyName: string;
  companySlogan: string;
}) => {
  return (
    <header id="header" className={styles.header}>
      <div>
        <h1>{companyName}</h1>
        <p>{companySlogan}</p>
      </div>
    </header>
  );
};

export default Header;