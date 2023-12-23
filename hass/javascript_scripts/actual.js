let api = require('@actual-app/api');

(async () => {
  await api.init({
    // Budget data will be cached locally here, in subdirectories for each file.
    dataDir: '.',
    // This is the URL of your running server
    serverURL: 'http://localhost:5006',
    // This is the password you use to log into the server
    password: '',
  });

  // This is the ID from Settings → Show advanced settings → Sync ID
  await api.downloadBudget('b8ea7c1c-10c5-46a5-ba28-5f104cef0471');
  // or, if you have end-to-end encryption enabled:
  // await api.downloadBudget('1cfdbb80-6274-49bf-b0c2-737235a4c81f', {
    // password: 'password1',
  // });

  let budget = await api.getBudgetMonth('2023-12');
  console.log(budget);
  await api.shutdown();
})();
