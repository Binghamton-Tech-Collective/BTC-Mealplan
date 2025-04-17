import { FontAwesome } from '@expo/vector-icons';
import { Stack } from 'expo-router';
import { View, Text, ScrollView } from 'react-native';


export default function Home() {
  return (
    <ScrollView className="flex-1 bg-white px-4 pt-10">
      {/* Header */}
      <View className="flex-row justify-between items-center mb-6">
        <Text className="text-2xl font-bold">Welcome, [NAME]</Text>
        <FontAwesome name='user-circle' size={32} color={"#333"} />
      </View>

      {/* Overview Section */}
      <Text className="text-lg font-semibold mb-3">Overview</Text>
      <View className="flex-row flex-wrap justify-between gap-2">

      </View>

      <View className="flex-row flex-wrap gap-8 m-8 mb-10">
        {/* Card placeholders */}
      <View className='w-40 h-40 rounded-lg bg-gray-200 items-center justify-center'/>
      <View className='w-40 h-40 rounded-lg bg-gray-200 items-center justify-center'/>
      <View className='w-40 h-40 rounded-lg bg-gray-200 items-center justify-center'/>
      <View className='w-40 h-40 rounded-lg bg-gray-200 items-center justify-center'/>
      </View>

      {/* Tracker */}
      <View className="bg-gray-200 rounded-t-3xl p-4">
        <Text className="text-base font-semibold mb-4">Spring 2025 Tracker</Text>
        <View className="h-32 bg-white border border-gray-300 rounded-md mb-6" />

        {/* Transactions */}
        <Text className="text-base font-semibold mb-4">Recent Transactions</Text>
        <View className="space-y-3 gap-2">
          <View className="h-12 bg-white border border-gray-300 rounded-md" />
          <View className="h-12 bg-white border border-gray-300 rounded-md" />
          <View className="h-12 bg-white border border-gray-300 rounded-md" />
        </View>
      </View>
    </ScrollView>
  );
}