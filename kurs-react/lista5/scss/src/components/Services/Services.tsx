import React from "react";
import styles from "./Services.module.scss";

const Services = ({
  services,
}: {
  services: {
    id: number;
    name: string;
    description: string;
  }[];
}) => {
  return (
    <div className={styles.services}>
      <h2>Our Services</h2>
      <ul>
        {services.map((service) => (
          <li key={service.id}>
            <h3>{service.name}</h3>
            <p>{service.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Services;
