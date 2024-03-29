import React from "react";
import styles from "./Section.module.scss";

const Section = ({
  children,
  id,
}: {
  children: React.ReactNode;
  id: string;
}) => {
  return (
    <section id={id} className={`${styles.section} ${id}`}>
      <div className={styles.sectionContent}>{children}</div>
    </section>
  );
};

export default Section;
