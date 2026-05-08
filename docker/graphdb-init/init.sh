#!/bin/bash

set -euo pipefail

GRAPHDB_URL="http://graphdb:7200"
REPO_ID="ontometal"

TTL_FILE="/rdf/ontometal.ttl"

/opt/graphdb/dist/bin/graphdb &
GRAPHDB_PID=$!

echo "⏳ Waiting GraphDB..."

for i in {1..30}; do
  if curl -s "$GRAPHDB_URL/rest/repositories" >/dev/null 2>&1; then
    echo "✅ GraphDB reachable"
    break
  fi
  sleep 2
done

echo "✅ GraphDB up"

# -----------------------
# CHECK REPOSITORY
# -----------------------
sleep 30 # Wait for GraphDB to be fully ready

echo "📦 Checking repository..."
REPOS_JSON=$(curl -s "$GRAPHDB_URL/rest/repositories")

if echo "$REPOS_JSON" | grep -q "\"$REPO_ID\""; then
  echo "📂 Repository already exists"
else
  echo "📦 Creating repository $REPO_ID"

  curl -X POST "$GRAPHDB_URL/rest/repositories" \
    -H "Content-Type: multipart/form-data" \
    -F "config=@/init/repo-config.ttl"

  echo "⏳ Waiting repository to be ready..."

  for i in {1..30}; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" \
      "$GRAPHDB_URL/repositories/$REPO_ID/statements")
  
    if [ "$STATUS" = "200" ]; then
      echo "✅ Repository ready"
      break
    fi
  
    echo "⏳ not ready yet ($i/30)"
    sleep 2
  done

  # -----------------------
  # LOAD TTL
  # -----------------------

  if [ -f "$TTL_FILE" ]; then
    echo "📥 Loading TTL..."

    curl -X POST \
      -H "Content-Type: text/turtle" \
      --data-binary "@$TTL_FILE" \
      "$GRAPHDB_URL/repositories/$REPO_ID/statements"

    echo "✅ TTL loaded"
  else
    echo "⚠️ TTL file not found: $TTL_FILE"
  fi
fi

echo "🚀 Initialization complete"