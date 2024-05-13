import React from "react";

interface BlogPostsProps {
  blogPosts: {
    id: number;
    title: string;
    date: string;
    content: string;
  }[];
}

const BlogPosts: React.FC<BlogPostsProps> = ({ blogPosts }) => {
  return (
    <>
      <h2 className="text-4xl mb-5 inline-block">Latest Blog Posts</h2>
      <div
        className="grid gap-5"
        style={{
          gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
        }}
      >
        {blogPosts.map((post) => (
          <div
            key={post.id}
            className="rounded-lg p-5 text-left bg-[#f0f0f0] text-[#333] dark:bg-[#222] dark:text-white"
          >
            <h3 className="mb-2">{post.title}</h3>
            <p className="mb-2">{post.date}</p>
            <p className="mb-2">{post.content}</p>
            <button className="border-none rounded-md cursor-pointer py-1 px-2 transition-colors duration-300 ease-in-out hover:bg-[#45a049] text-white bg-[#4caf50] dark:bg-[#4caf50] dark:hover:bg-[#45a049]">
              Read More
            </button>
          </div>
        ))}
      </div>
    </>
  );
};

export default BlogPosts;
