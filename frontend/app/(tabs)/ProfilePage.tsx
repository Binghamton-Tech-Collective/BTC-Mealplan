import { Stack } from 'expo-router';
import { View } from 'react-native';


export default function Profile() {
  return (
    <>
      <Stack.Screen options={{ title: 'Profile' }} />
      <View className="flex-1 p-6">
        
      </View>
    </>
  );
}

