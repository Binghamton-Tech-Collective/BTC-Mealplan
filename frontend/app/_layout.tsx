import '../global.css';

import { Stack } from 'expo-router';

// import LoadingPage from './LoadingPage';

// export default function LoadingScreen() {
//   return <LoadingPage/>;
// }

// import LoginPage from './LoginPage';

// export default function LoginScreen() {
//   return <LoginPage/>;
// }

export const unstable_settings = {
  // Ensure that reloading on `/modal` keeps a back button present.
  initialRouteName: '(tabs)',
};

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
      <Stack.Screen name="modal" options={{ presentation: 'modal' }} />
    </Stack>
  );
}
