// ip_objects.js
import { validateIPAddress } from "./ip_objects";

const form = document.querySelector("form");
form.addEventListener("submit", (event) => {
  event.preventDefault();

  const ipAddress = document.querySelector("#ip_address").value;

  try {
    const isValid = validateIPAddress(ipAddress);
    if (isValid) {
      alert("The IP address is valid!");
    } else {
      alert("The IP address is invalid!");
    }
  } catch (error) {
    console.error(error);
    alert("An error occurred while trying to validate the IP address.");
  }
});