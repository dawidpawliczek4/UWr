import React from "react";

interface ServicesProps {
    services: {
        id: number;
        name: string;
        description: string;
    }[];
}

const Services: React.FC<ServicesProps> = ({
    services
}) => {
  return (
    <div>      
      <h2 className="text-4xl mb-5 inline-block">Our Services</h2>
      <ul className="p-0 m-0">
        {services.map((service) => (
          <li key={service.id} className="mb-5 text-left">
            <h3 className="text-3xl mb-2">{service.name}</h3>
            <p>{service.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Services;
