import React from "react";
import styles from "./TeamMembers.module.scss";

interface TeamMembersProps {
  teamMembers: {
    id: number;
    name: string;
    position: string;
    bio: string;
    image: string;
  }[];
}

const TeamMembers: React.FC<TeamMembersProps> = ({ teamMembers }) => {
  return (
    <>
      <h2>Meet Our Team</h2>
      <div className={styles.teamMembers}>
        {teamMembers.map((member) => (
          <div key={member.id} className={styles.teamMember}>
            <img src={member.image} alt={member.name} />
            <div>
              <h3>{member.name}</h3>
              <p>{member.position}</p>
              <p>{member.bio}</p>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default TeamMembers;
