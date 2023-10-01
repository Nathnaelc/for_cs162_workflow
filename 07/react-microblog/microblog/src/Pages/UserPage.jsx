import { useParams } from "react-router-dom";
import Body from "../components/Body";
import Posts from "../components/Posts";

export default function UserPage() {
  const { username } = useParams();

  return (
    <Body sidebar>
      {user === undefined ? (
        <Spinner animation="border" />
      ) : (
        <>
          {user === null ? (
            <p>Could not retrieve blog posts.</p>
          ) : (
            <>
              {/* ... user details */}
              <Posts content={user.id} />
            </>
          )}
        </>
      )}
    </Body>
  );
}
