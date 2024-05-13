import React from "react";

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
      <h2 className="text-4xl mb-5 inline-block">Meet Our Team</h2>
      <div className="flex flex-wrap justify-center bg-[#f5f5f5] text-[#333] dark:bg-[#444] dark:text-white">
        {teamMembers.map((member) => (
          <div
            key={member.id}
            className="flex-grow-0 flex-shrink-0 p-5 m-2 text-center"
            style={{
              flexBasis: "calc(33.33% - 20px)",
            }}
          >
            <img
              src={member.image}
              alt={member.name}
              className="rounded-full mb-5"
            />
            <div>
              <h3 className="mb-2 inline-block">{member.name}</h3>
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
