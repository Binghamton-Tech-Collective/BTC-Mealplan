import * as SecureStore from 'expo-secure-store';
import { useState } from 'react';
import { View } from 'react-native';

import { Button } from '@/components/ui/button';
import { Text } from '@/components/ui/text';
import { SECURE_STORE_KEYS } from '@/constants/secureStoreKeys';

export default function HomeScreen() {
  const [info, setInfo] = useState('');

  async function getInfo() {
    const email = await SecureStore.getItemAsync(SECURE_STORE_KEYS.email);
    const password = await SecureStore.getItemAsync(SECURE_STORE_KEYS.password);
    setInfo(`Email: ${email}\nPassword: ${password}`);
  }

  return (
    <View className="flex-1 items-center justify-center gap-5">
      <Text className="text-2xl">Home</Text>
      <Button onPress={getInfo}>
        <Text>Get Info</Text>
      </Button>
      <Text>{info}</Text>
    </View>
  );
}
