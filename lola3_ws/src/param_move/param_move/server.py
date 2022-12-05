#!/usr/bin/env python

import rclpy
from .server_class import Service


def main(args=None) -> None:
    rclpy.init(args=args)

    service = Service()

    rclpy.spin(service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
