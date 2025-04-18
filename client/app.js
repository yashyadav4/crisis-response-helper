document.getElementById("crisisForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const type = document.getElementById("type").value;

  navigator.geolocation.getCurrentPosition(async (position) => {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    const res = await fetch("https://crisis-api.onrender.com/crisis", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ type, lat, lon })
    });

    const data = await res.json();
    document.getElementById("response").innerText = data.response;
    if (data.places && data.places.length > 0) {
      const nearby = data.places.map(p => `<li>${p}</li>`).join("");
      document.getElementById("nearby").innerHTML = "<h3>Nearby Help Centers:</h3><ul>" + nearby + "</ul>";
    }
  });
});
