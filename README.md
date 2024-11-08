# BOT GRASS AUTO FARMING GUIDE

Stay updated and join our Telegram community: [@shadowscripters](https://t.me/shadowscripters)

---

## 📥 Grass Bot Registration & Setup
1. **Register**: [Grass App Registration](https://app.getgrass.io/register?referralCode=Qj0nK0iL4SRgIT8)
2. **Choose a Version**:
   - **Lite Version**: For lightweight usage, log in with the Lite extension.
   - **Node Version**: For more complex setups, log in with the Node extension.

   > **Note**: Use only one version at a time. The proxy format is already provided in `localproxies.txt` as an example.

3. **Current Dashboard Status**: The Grass Dashboard may show errors (as per the Grass team on Discord), but your points will still accumulate correctly.

---

## 🛠️ Requirements & Installation

Run the following commands to set up your environment:

```bash
git clone https://github.com/ShadowScripts1/GRASS.git
cd GRASS
pip install requests loguru fake_useragent websockets==12.0 websockets_proxy
```

### Running the Bot
- For Node: `python localgrassnode.py`
- For Lite: `python localgrasslite.py`

---

## 🔍 How to Retrieve Your Grass User ID

1. **Log in** to the Grass web app.
2. Open **Developer Tools**:
   - Right-click > Inspect or press `F12`.
3. Go to the **Console** tab and paste the following command:
   ```javascript
   localStorage.getItem('userId')
   ```
4. If pasting doesn’t work:
   - Type `allow pasting` and press Enter.
   - Then paste and run `localStorage.getItem('userId')` again.

---

Feel free to reach out to the community on Telegram if you need further assistance!