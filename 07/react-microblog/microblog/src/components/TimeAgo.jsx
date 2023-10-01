import { useState, useEffect } from "react";

export default function TimeAgo({ isoDate }) {
  const [timeAgo, setTimeAgo] = useState("");

  useEffect(() => {
    const intervalId = setInterval(() => {
      const now = new Date();
      const postDate = new Date(isoDate);
      const secondsAgo = Math.round((now - postDate) / 1000);
      // ... compute timeAgo string based on secondsAgo
      setTimeAgo(/* computed string */);
    }, 60000); // update every minute

    return () => clearInterval(intervalId);
  }, [isoDate]);

  return <span title={new Date(isoDate).toString()}>{timeAgo}</span>;
}
