import React from "react";
import Button from "react-bootstrap/Button";

function More({ pagination, loadNextPage }) {
  // Determine if there are more items to load
  const thereAreMore = pagination
    ? pagination.offset + pagination.count < pagination.total
    : false;

  return (
    <div className="More">
      {thereAreMore && (
        <Button variant="outline-primary" onClick={loadNextPage}>
          More &raquo;
        </Button>
      )}
    </div>
  );
}

export default More;
