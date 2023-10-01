import { Link } from "react-router-dom";
import TimeAgo from "./TimeAgo";

export default function Post({ post }) {
  return (
    <div className="d-flex align-items-start mb-2">
      <img
        src={post.author.avatar_url + "&s=48"}
        alt={post.author.username}
        className="rounded-circle me-2"
      />
      <div>
        <p>
          <Link to={"/user/" + post.author.username}>
            {post.author.username}
          </Link>
          &nbsp;—&nbsp;
          <TimeAgo isoDate={post.timestamp} />
        </p>
        <p>{post.text}</p>
      </div>
    </div>
  );
}
