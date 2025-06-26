<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thank You</title>
  <style>
    body {
      font-family: 'Segoe UI', Arial, sans-serif;
      background: linear-gradient(135deg, #6366f1 0%, #f1f5f9 100%);
      margin: 0;
      padding: 0;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    h2 {
      text-align: center;
      color: #22223b;
      padding: 2.5rem 2rem;
      background: rgba(255, 255, 255, 0.92);
      border-radius: 18px;
      box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: 1px;
      opacity: 0;
      transform: translateY(20px) scale(0.98);
      transition: opacity 0.7s cubic-bezier(.4,2,.6,1), transform 0.7s cubic-bezier(.4,2,.6,1);
      backdrop-filter: blur(2px);
    }

    .visible {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    @media (max-width: 600px) {
      h2 {
        font-size: 1.2rem;
        padding: 1.2rem 1rem;
      }
    }
  </style>
</head>
<body>

  <h2 id="thankYouMessage">Thanks for trying this Project.<br>You can verify data in DynamoDB Table.</h2>

  <script>
    const thankYouMessage = document.getElementById('thankYouMessage');
    setTimeout(() => {
      thankYouMessage.classList.add('visible');
    }, 500);
  </script>

</body>
</html>
