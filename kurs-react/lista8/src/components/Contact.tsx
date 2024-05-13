import React from "react";

interface ContactProps {
  handleSubmit: (event: React.FormEvent<HTMLFormElement>) => void;
}

const Contact: React.FC<ContactProps> = ({ handleSubmit }) => {
  return (
    <div className="mb-10">
      <h2 className="text-4xl mb-5 inline-block">Contact Us</h2>
      <form
        onSubmit={handleSubmit}
        className="max-w-[500px] my-0 mx-auto p-5 rounded-lg flex flex-col bg-[#f9f9f9] text-[#333] border-[1px] border-solid border-[#ddd] dark:bg-[#333] dark:text-white dark:border-[#555]"
      >
        <div className="mb-5">
          <input
            type="text"
            placeholder="Name"
            className="p-2 rounded-md border-none mt-1 w-[calc(100% - 20px)] bg-white text-[#333] border-[1px] border-solid border-[#ccc] dark:bg-[#444] dark:text-white dark:border-[#666]"
            required
          />
        </div>
        <div className="mb-5">
          <input
            type="email"
            placeholder="Email"
            className="p-2 rounded-md border-none mt-1 w-[calc(100% - 20px)] bg-white text-[#333] border-[1px] border-solid border-[#ccc] dark:bg-[#444] dark:text-white dark:border-[#666]"
            required
          />
        </div>
        <div className="mb-5">
          <textarea
            rows={5}
            placeholder="Message"
            className="p-2 rounded-md border-none mt-1 w-[calc(100% - 20px)] resize-y bg-white text-[#333] border-[1px] border-solid border-[#ccc] dark:bg-[#444] dark:text-white dark:border-[#666]"
            required
          ></textarea>
        </div>
        <button
          className="py-2 px-5 border-none rounded-md cursor-pointer transition-colors duration-300 ease-in-out bg-[#4caf50] text-white hover:bg-[#45a049]"
          type="submit"
        >
          Send Message
        </button>
      </form>
    </div>
  );
};

export default Contact;
