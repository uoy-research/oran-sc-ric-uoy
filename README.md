# Custom OSC RIC for VIAVI Tester

<a href="https://drive.google.com/file/d/1-q2HnX_2NywSyFFV06pchVEcJUlWvjjs/view?usp=sharing" target="_blank"><h1>Demo of the setup</h1></a>

## Running the OSC RIC

1. **Clone the repository** (ideally on the same machine where the VIAVI tester is running):

2. Navigate to the repository directory:

3. Launch the RIC:
   ```bash
   sudo docker compose up --build
   ```
4. Find the IP address of the `e2term` service:
   ```bash
   sudo docker ps
   ```
   The `e2term` service acts as the entry and exit point into the RIC. Use its IP address as the IP address of the RIC.

Once the RIC is up and running, you can proceed to connect it to the VIAVI tester.

---

## Running the RIC with VIAVI Tester

1. Import the <a href="https://drive.google.com/file/d/1eVYKS44vsNUCKpoOfP1L7tQbFnf6i04S/view?usp=sharing" targer="_blank">provided configuration</a> file into the **E2 Interface Testing** section of the VIAVI tester.

   - Note: Even though the configuration is imported in the **E2 Interface Testing** section, the settings will apply across the entire tester.

2. Adjust parameters as needed and save the configuration for future use.

3. Run the **Simulation** in the VIAVI tester.

   - If the connection is successful, an **Association** message will appear in the console where you ran the RIC.

4. To run the xApp, execute the following command:

   ```bash
   sudo docker compose exec python_xapp_runner ./kpm_mon_xapp.py --metrics=DRB.UEThpDl --kpm_report_style=3 --e2_node_id="gnb_001_001_123456"
   ```

   The xApp will subscribe to `DRB.UEThpDl` measurements and display the content of received `RIC_INDICATION` messages. Example console output:

   ```
   RIC Indication Received from gnb_001_001_0000019b for Subscription ID: 65
   E2SM_KPM RIC Indication Content:
   - CollectStartTime:  2024-01-26 00:08:05
   - Measurements Data:
     - Metric: DRB.UEThpDl, Value: 4
   ```

5. To create your own xApp:

   - Add your code in the `xApps/python/` folder.
   - After making changes, restart and rebuild the RIC to apply updates:

     ```bash
     sudo docker compose down
     sudo docker compose up --build

     ```
