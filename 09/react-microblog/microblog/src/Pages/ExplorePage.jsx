import Body from "../components/Body"; // Import the Body component if it exists
import Posts from "../components/Posts";

export default function ExplorePage() {
  return (
    <Body sidebar>
      <Posts content="explore" />
    </Body>
  );
}
