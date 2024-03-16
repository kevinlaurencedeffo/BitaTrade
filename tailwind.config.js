/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'static/css/*.css',
    'templates/*.html',
    'templates/auth/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        Poppins: "Poppins",
      },
    },
  },
  plugins: [],
}

