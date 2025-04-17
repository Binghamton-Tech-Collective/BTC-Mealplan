import { Link, Tabs } from 'expo-router';

import { TabBarIcon } from '../../components/TabBarIcon';

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: 'black',
      }}>
      
      <Tabs.Screen
        name="HomePage"
        options={{
          title: 'Home',
          tabBarIcon: ({ color }) => <TabBarIcon name="code" color={color} />,
        }}
      />
      <Tabs.Screen
        name="FoodPage"
        options={{
          title: 'Food',
          tabBarIcon: ({ color }) => <TabBarIcon name="code" color={color} />,
        }}
      />
      <Tabs.Screen
        name="ProfilePage"
        options={{
          title: 'Profile',
          tabBarIcon: ({ color }) => <TabBarIcon name="code" color={color} />,
        }}
      />
    </Tabs>
  );
}
