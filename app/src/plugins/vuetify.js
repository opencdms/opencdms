// Styles
import '@mdi/font/css/materialdesignicons.css'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

// Vuetify
import { createVuetify } from "vuetify";

export default createVuetify({
  icons: {
    defaultSet: "mdi",
    aliases,
    sets: {
      mdi,
    },
  },
  theme: {
    themes: {
      light: {
        dark: false,
        primary: "#014e9e",
        secondary: "#75b942",
        accent: "#d5e3f0",
        warning: "#f8a700",
        error: "#B00020"
      },
      dark: {
        light: false,
        primary: "#01aad3",
        secondary: "#75b942",
        accent: "#d5e3f0",
        warning: "#f8a700",
        error: "#B00020"
      },
    }
  },
});
