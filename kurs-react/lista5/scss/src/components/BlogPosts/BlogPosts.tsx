import React from "react";
import styles from "./BlogPosts.module.scss";

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
      <h2>Latest Blog Posts</h2>
      <div className={styles.blogPosts}>
        {blogPosts.map((post) => (
          <div key={post.id} className={styles.blogPost}>
            <h3>{post.title}</h3>
            <p>{post.date}</p>
            <p>{post.content}</p>
            <button>Read More</button>
          </div>
        ))}
      </div>
    </>
  );
};

export default BlogPosts;
